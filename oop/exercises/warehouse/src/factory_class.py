from worker import DeliveryMan, Packager


# Complete the method create_object
class WorkerFactory:
    @staticmethod
    def create_object(worker_type):
        try:
            if worker_type == "packager":
                return Packager()
            elif worker_type == "delivery":
                return DeliveryMan()
            # else:
            #     raise AssertionError('Invalid worker type.')
        except AssertionError as e:
            print(str(e))
           
        




