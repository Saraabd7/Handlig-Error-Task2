class New_users():

    def __init__(self, name):
        self.name = name





    def output_text_file(self,file_name):
        try:
            with open(file_name, 'w+') as file_to_create:
                file_to_create.write(f'User name: {self.name}')

        except TypeError as error:
            print('Ensure you have printed all arguments')
            print(error)

        finally:
            print(' Execution done! Program is now closing')
