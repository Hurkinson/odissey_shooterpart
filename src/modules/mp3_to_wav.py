from pydub import AudioSegment
import subprocess
                
                                                                      
src_path = r"Assets\Music\raw\luna.mp3"

dst_name = "test"
dst_format = "wav"
dst_path = r"Assets\Music\wav\\" + dst_name + "." + dst_format


subprocess.call(['ffmpeg', '-i', src_path,dst_path])                                                    
sound = AudioSegment.from_mp3(src_path)
sound.export(dst_path, format=dst_format)