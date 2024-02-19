from flask import Flask

FAI=Flask(__name__)

@FAI.route('/stringresponse')
def stringsresponse():
    return 'Evadra nu intha talentedga unnav'


if __name__=='__main__':
    FAI.run(debug=True)