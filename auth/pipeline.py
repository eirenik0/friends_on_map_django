def get_user_avatar(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    url = None
    if getattr(backend, 'name', None) == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
 
    if url:
        avatar = url
        social_user.set_extra_data({'photo': url})
        social_user.save()