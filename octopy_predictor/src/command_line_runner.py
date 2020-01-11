''' CLI RUNNER'''
from context import *

if __name__ == '__main__':

    init_dependencies()
    interface = app_context['CommandShellInterface']

    # interface.greet(username)

    # # interface.get_input_options()
    # interface.option_selected_hash = input("Enter any 1 of the above options:")
    # print(interface.option_selected_hash)
    # print("You have selected Option {0} from the above options.".format(interface.option_selected_hash))
    # path = input("please enter/ paste local path:\n")

    path = r"..\data\nifty50.csv"
    interface.load_data(path = path)
    interface.get_columns()
    interface.set_features_and_labels()
    interface.get_features_and_labels()
    interface.get_model_ids()
    interface.train(0.8)
 
