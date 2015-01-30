from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from userprofile import utils
from userprofile.models import UserProfile
from userprofile.forms import FormUserProfileUpadte, FormUserUpdate

# Create your views here.

@login_required
def update_profile(request,
                   success_url=None,
                   template_name='profiles/edit_profile.html',
                   extra_context=None):
    '''
    This is the View that is used to update the user profile
    '''
    try:
        profile_obj = request.user
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('userprofile_ditail_profile'))

    if success_url is None:
        success_url = reverse('userprofile_ditail_profile')
    if request.method == 'POST':
        formuser = FormUserUpdate(data=request.POST, instance=request.user) # pylint: disable=E1120,E1123
        instance = UserProfile.objects.get(user=profile_obj) # pylint: disable=E1101
        formuserprofile = FormUserProfileUpadte(data=request.POST, instance=instance) # pylint: disable=E1120,E1123
        if formuser.is_valid() and formuserprofile.is_valid(): # pylint: disable=E1101
            formuser.save() # pylint: disable=E1101
            formuserprofile.save() # pylint: disable=E1101
            return HttpResponseRedirect(reverse('userprofile_ditail_profile'))
    else:
        formuser = FormUserUpdate(instance=profile_obj) # pylint: disable=E1120,E1123
        instance = UserProfile.objects.get(user=profile_obj) # pylint: disable=E1101
        formuserprofile = FormUserProfileUpadte(instance=instance) # pylint: disable=E1120,E1123
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
                              {'form': formuser,
                               'formuser': formuserprofile,
                               'profile': profile_obj},
                              context_instance=context)

@login_required
def ditail_profile(request,
                   public_profile_field=None,
                   template_name='profiles/detail_profile.html',
                   extra_context=None):
    '''
    This is the viw that is user do display the user profile
    '''
    user = request.user
    try:
        # pylint: disable=E1101
        profile_obj = UserProfile.objects.get(user=user)
        # pylint: enable=E1101
    except ObjectDoesNotExist:
        profile_obj = utils.create_profile(user=user)

    if public_profile_field is not None and \
    not getattr(profile_obj, public_profile_field):
        profile_obj = None

    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value

    return render_to_response(template_name,
                              {'profile': profile_obj},
                              context_instance=context)
