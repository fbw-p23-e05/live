class CatController:

    # TODO: You need to write the code for this class based on what the tests
    # expect.

    def hourly_run(self, hour):
        self.hour = hour

        if self.hour == 7:
            return "Open cat cage."
        
        elif self.hour == 8:
            return "Give water. Feed 1 mouse."
        
        elif self.hour in [9, 10, 11, 13, 14, 15, 16, 18, 19]:
            return "Give water."
   
        # elif self.hour == 9:
        #     return "Give water."
        
        # elif self.hour == 10:
        #     return "Give water."
        
        # elif self.hour == 11:
        #     return "Give water."
        
        elif self.hour == 12:
            return "Feed 1 hamster."
        elif self.hour == 17:
            return "Give water. Feed 1 chicken."
        elif self.hour == 20:
            return "Close cat cage."
        else:
            return ''
        

        

        

        

        
        

