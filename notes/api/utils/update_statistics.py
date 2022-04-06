from customAdmin.models import DailyStatistics

"""
def mobile_api_requests(*args):

    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.save()

    if "description" in args[0]:
        device = args[0]["device"]
        description = args[0]["description"]

        DeviceAction.objects.create(device=args[0]["device"], description="{} {} {}".format(device.brand, device.model, description))


def new_device(*args):

    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.app_launched_count += 1
    daily_statistics_object.new_devices += 1
    daily_statistics_object.save()


def app_launched_count(*args):

    device = args[0]["device"]
    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.app_launched_count += 1
    daily_statistics_object.save()

    DeviceAction.objects.create(device=device, description="{} {} abriu a aplicação movel".format(device.brand, device.model))


def personal_note_create(*args):

    device = args[0]["device"]
    article = args[0]["article"]
    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.personal_notes_created += 1
    daily_statistics_object.save()

    DeviceAction.objects.create(device=device, description="{} {} adicionou o artigo {} as suas notas pessoais".format(device.brand, device.model, article.__str__()))


def personal_note_edit(*args):

    device = args[0]["device"]
    personal_note = args[0]["personal_note"]
    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.personal_notes_edited += 1
    daily_statistics_object.save()

    DeviceAction.objects.create(device=device, description="{} {} editou a sua nota pessoal {}".format(device.brand, device.model, personal_note.__str__()))


def personal_note_entry(*args):

    device = args[0]["device"]
    personal_note = args[0]["personal_note"]
    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.personal_notes_entries += 1
    daily_statistics_object.save()

    DeviceAction.objects.create(device=device, description="{} {} abriu a sua nota pessoal {}".format(device.brand, device.model, personal_note.__str__()))


def personal_notes_deleted(*args):

    device = args[0]["device"]
    delete_count = args[0]['delete_count']
    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.save()

    DeviceAction.objects.create(device=device, description="{} {} eliminou {} notas pessoais".format(device.brand, device.model, delete_count))


def article_entry(*args):

    device = args[0]["device"]
    article = args[0]["article"]
    daily_statistics_object = DailyStatistics.get_today_model()
    daily_statistics_object.mobile_api_requests += 1
    daily_statistics_object.article_entries += 1
    daily_statistics_object.save()

    DeviceAction.objects.create(device=device, description="{} {} abriu {}".format(device.brand, device.model, article.__str__()))
"""