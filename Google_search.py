'''
    Performing google search using Python code
'''
class Google_search:

    def __init__(self,name_search):
        self.name = name_search

    def google_search(self):
        count = 0
        try :
            from googlesearch import search
        except ImportError:
            print("No Module named 'google' Found")

        for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
            count += 1
            print (count)
            print(i + '\n')


if __name__=='__main__':
    gs = Google_search("Data science")
    gs.google_search()