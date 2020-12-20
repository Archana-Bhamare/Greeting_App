from django.shortcuts import render, redirect
# Create your views here.
from greet_app.forms import GreetingForm
from greet_app.models import Person
import logging

# Create and Configure logger
LOG_FORMAT = "%(levelname)s - %(asctime)s - %(message)s"
logging.basicConfig(filename= "C:\\Users\\KatK\\django_projects\\greeting_project\\static\\logtest.log", level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger()

def insert(request):
    """

    :param request: Enter the name and message
    :return: Insert data
    """
    logger.debug("# User name and message inserted")
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Your data has been successfully inserted")
            return redirect('/show')
    return render(request, 'insert.html')


def show(request):
    """

    :param request: Show all the user card
    :return: display all the user card
    """
    logger.debug("# Display all the user data")
    greet = Person.objects.all()
    logger.info("Display all the Data")
    return render(request, 'show.html', {'greet': greet})


def delete(request, id):
    """

    :param request: for particular user_id delete
    :param id: User_id
    :return: deleted the particular user_id
    """
    logger.debug("# Delete the data")
    greet = Person.objects.get(id=id)
    greet.delete()
    logger.info("your data has been successfully deleted")
    return redirect('/show')


def update(request, id):
    """

    :param request: for particular user_id update
    :param id: user_id
    :return: updated particular user_id
    """
    logger.debug("# Update the data")
    greet = Person.objects.get(id=id)
    form = GreetingForm(request.POST, instance=greet)
    if form.is_valid():
        form.save()
        logger.info("your data has been successfully updated")
        return redirect('/show')
    return render(request, 'update.html', {'greet': greet})
