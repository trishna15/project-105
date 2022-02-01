import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A--Sj4BqI9JXXJkci9Zct7uo4peNTPy_trEaowgZ_jmp_2sm-rwGv59m6m3sKnX7BqjxfLuDE9Tvd9kero98rqfcLe6EVGqLdBHKS-RFxE9B-Hhy2L8QcIf0WGa9RPTrvyzDtyg'
    transferData = TransferData(access_token)

    file_from = 'class.py'
    file_to = '/class.py'

    transferData.upload_file(file_from, file_to)
    print("The file has moved.")
if __name__ == '__main__':
    main()