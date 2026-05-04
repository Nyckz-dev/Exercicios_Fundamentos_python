import time
import threading 

class StopWatch:
      def __init__(self, start):
         self.start = start
         self.current = start
         self.running = False
         self.thread = None
    
      def _run(self):
        while self.current >= 0 and self.running:
            print(self.current)
            time.sleep(1)
            self.current -= 1
        self.running = False
    
      def start_countdown(self):
       if not self.running:
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()
      
      def pause(self):
         self.running = False
         print("Countdown paused at: ", self.current)

      def reset(self):
         self.running = False
         self.current = self.start
         print("Countdown reset to: ", self.start)
      
      


           
       
