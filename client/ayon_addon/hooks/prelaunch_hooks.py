from ayon_applications import PreLaunchHook

class MyHook(PreLaunchHook):
    order = 15         # Where the hook should be ordered among the other hooks
    app_groups = {}    # Run for all apps
    launch_types = {}  # Run always

    def execute(self):
        
        print("My Prelaunch hook is running!")
        
        print("Launch Context Data:")
        print(self.launch_context.data)
        
        print("Launch args:")
        print(self.launch_context.launch_args)
        
        print("Launch environment:")
        print(self.launch_context.env)
        
        # Adding your own custom env var
        self.launch_context.env["MY_CUSTOM_ENV_VAR"] = "my_custom_value"