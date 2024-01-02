from server_errors import OK, NotFound, ServerError

# Write code to test your classes

objects = [OK(), NotFound(), ServerError()]

def status(error_object):
    # obj_1 = OK()
    # print(obj_1.code)
    # print(obj_1.message)

    for obj in error_object:
        print({'code': obj.code, 'message': obj.message})

status(objects)