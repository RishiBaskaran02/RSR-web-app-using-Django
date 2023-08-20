from APP.models import signin, Verification

def UserAccountDetails(request):
    data = signin.objects.filter(fullname = request.session.get('username'))
    return {
        'AccountData' : data
    }
def toVerifyData(request):
    data = Verification.objects.all
    return {
        'toVerifyData' : data
    }
def userVerificationSubmitted(request):
    CurrentUser = request.session.get('username')
    userSubmitted =0
    record = Verification.objects.filter(fullname= CurrentUser)
    if(len(record) ==0):
        userSubmitted = 0
    else: 
        userSubmitted = 1
    return {
        'userSubmitted' : userSubmitted
    }
def userIsVerified(request):
    CurrentUser = request.session.get('username')
    userVerified =0
    record = Verification.objects.filter(fullname= CurrentUser)
    try:
        if record.first().verified == 0:
            userVerified = 0
        else:
            userVerified = 1
    except: pass
    return {
        'userVerified' : userVerified
    }