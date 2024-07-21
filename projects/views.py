from django.shortcuts import render
from projects.models import Projects, Participant
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ParticipantForm
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
# Create your views here.

paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)
def project_index(request):
    projects = Projects.objects.all()
    context = { 'projects':projects }
    return render(request,'project_index.html',context)

def project_detail(request,pk):
    project = Projects.objects.get(pk=pk)
    context = {  'project': project }
    return render(request,'project_detail.html',context)




def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            
            reference=f"{participant.id}"
            response = Transaction.initialize(
                reference=reference,
                amount= 10000*100,
                email=participant.email,
                callback_url=request.build_absolute_uri(reverse('projects:payment_confirmation'))
            )
            if response['status']:
                    auth_url = response['data']['authorization_url']
                    return redirect(auth_url)
            else:
                return HttpResponse("Payment initialization failed. Please try again.")
            # return redirect(response['data']['authorization_url'])
    else:
        form = ParticipantForm()
    return render(request, 'registration/register.html', {'form': form})
@csrf_exempt
def payment_confirmation(request):
    
    reference = request.GET.get('reference')
    transaction = Transaction.verify(reference=reference)
    if transaction['data']['status'] == 'success':
        participant_id = int(reference)
        participant = Participant.objects.get(id=participant_id)
        send_mail(
            'Registration Confirmation',
            f"Hello {participant.name}, your registration for the Python Coding class is successful.\n A whatsapp link will be send to you later to join the coding class group.\n For more information call 07084855701.\n Best Regards,\n PyTechMentors",
            settings.EMAIL_HOST_USER,
            [participant.email],
            fail_silently=False,
        )
        return render(request, 'registration/confirmation.html', {'participant': participant})
    return render(request, 'registration/failed.html')
