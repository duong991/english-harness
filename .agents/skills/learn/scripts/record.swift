import Foundation
import AVFoundation

struct AudioRecorderCLI {
    static func printUsage() {
        print("""
        Usage: record-audio [options]
        
        Options:
          -d, --duration <seconds>    Duration to record in seconds (default: 60, or 0 for manual stop)
          -o, --output <filepath>     Output audio file path (default: artifacts/audio/YYYY-MM-DD-HHMMSS.m4a)
          -t, --topic <name>          Topic name for auto-generated file naming
          -h, --help                  Show this help message
          
        Examples:
          record-audio -d 60
          record-audio -d 120 -t project-pitch
          record-audio -o artifacts/audio/my-speech.m4a
        """)
    }
    
    static func parseArguments() -> (duration: Double, outputPath: String, topic: String) {
        var duration: Double = 60.0
        var outputPath: String = ""
        var topic: String = "speaking"
        
        let args = CommandLine.arguments
        var i = 1
        while i < args.count {
            let arg = args[i]
            switch arg {
            case "-d", "--duration":
                if i + 1 < args.count, let val = Double(args[i + 1]) {
                    duration = val
                    i += 1
                }
            case "-o", "--output":
                if i + 1 < args.count {
                    outputPath = args[i + 1]
                    i += 1
                }
            case "-t", "--topic":
                if i + 1 < args.count {
                    topic = args[i + 1].replacingOccurrences(of: " ", with: "-").lowercased()
                    i += 1
                }
            case "-h", "--help":
                printUsage()
                exit(0)
            default:
                break
            }
            i += 1
        }
        
        if outputPath.isEmpty {
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy-MM-dd-HHmmss"
            let timestamp = formatter.string(from: Date())
            outputPath = "artifacts/audio/\(timestamp)-\(topic).m4a"
        }
        
        return (duration, outputPath, topic)
    }
    
    static func run() {
        let (duration, outputPath, _) = parseArguments()
        
        let outputURL = URL(fileURLWithPath: outputPath)
        let outputDir = outputURL.deletingLastPathComponent()
        
        do {
            try FileManager.default.createDirectory(at: outputDir, withIntermediateDirectories: true, attributes: nil)
        } catch {
            print("❌ Error creating output directory: \(error.localizedDescription)")
            exit(1)
        }
        
        let settings: [String: Any] = [
            AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
            AVSampleRateKey: 44100.0,
            AVNumberOfChannelsKey: 1,
            AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue,
            AVEncoderBitRateKey: 64000
        ]
        
        let recorder: AVAudioRecorder
        do {
            recorder = try AVAudioRecorder(url: outputURL, settings: settings)
        } catch {
            print("❌ Failed to initialize audio recorder: \(error.localizedDescription)")
            exit(1)
        }
        
        guard recorder.prepareToRecord() else {
            print("❌ Failed to prepare audio recording. Check microphone permissions.")
            exit(1)
        }
        
        guard recorder.record() else {
            print("❌ Failed to start recording. Please grant microphone access to your terminal / IDE.")
            exit(1)
        }
        
        print("🎙️ Recording started! Output: \(outputPath)")
        if duration > 0 {
            print("⏱️ Target duration: \(Int(duration))s (Press [Enter] anytime to finish early)")
        } else {
            print("⏱️ Recording indefinitely (Press [Enter] to stop)")
        }
        
        var isRecording = true
        let startTime = Date()
        
        // Background thread to listen for Enter key to stop early
        DispatchQueue.global(qos: .userInitiated).async {
            _ = readLine()
            isRecording = false
        }
        
        // Progress display loop
        while isRecording {
            let elapsed = Date().timeIntervalSince(startTime)
            if duration > 0 && elapsed >= duration {
                break
            }
            
            let elapsedSec = Int(elapsed)
            let mins = elapsedSec / 60
            let secs = elapsedSec % 60
            
            if duration > 0 {
                let totalSec = Int(duration)
                let totalMins = totalSec / 60
                let totalRemSecs = totalSec % 60
                let progressPercent = min(100, Int((elapsed / duration) * 100))
                let barLength = 20
                let filledLength = Int((Double(progressPercent) / 100.0) * Double(barLength))
                let bar = String(repeating: "█", count: filledLength) + String(repeating: "░", count: barLength - filledLength)
                
                print(String(format: "\r🎤 [%02d:%02d / %02d:%02d] |%@| %3d%%", mins, secs, totalMins, totalRemSecs, bar, progressPercent), terminator: "")
            } else {
                print(String(format: "\r🎤 [%02d:%02d] Recording... (Press Enter to finish)", mins, secs), terminator: "")
            }
            fflush(stdout)
            
            Thread.sleep(forTimeInterval: 0.2)
        }
        
        recorder.stop()
        print("\n\n✅ Recording finished and saved!")
        
        if let attrs = try? FileManager.default.attributesOfItem(atPath: outputPath),
           let fileSize = attrs[.size] as? Int64 {
            let kb = Double(fileSize) / 1024.0
            print("📁 File: \(outputPath) (\(String(format: "%.1f", kb)) KB)")
        } else {
            print("📁 File: \(outputPath)")
        }
        print("🎯 Audio is ready for AI analysis!")
    }
}

AudioRecorderCLI.run()
