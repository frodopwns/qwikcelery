Playing with Celery
====================

This VM comes prepped and ready to run celery as a daemon using the tasks found in /data/code (myapp.py).

SSH into the VM like so:

    qwikcelery$ vagrant ssh

Once logged in you will need to run this command to start teh celery daemon:

    sudo /etc/init.d/celeryd start


For your convenience I have included a very basic celery app with this development environment. In the code directory of thid repository or /data/code on the host0.celery vm you can find a file named myapp.py.

In myapp.py there is a celery task named add:

    @app.task
    def add(x, y):
        return x + y
        
Now we are going to test this task using the python interactive interpreter.  First cd to /data/code on the VM.

Type `python` to enter the interreter

run these commands:

    from myapp import add
    add.delay(10,4)
    quit()

Not from the command line run `cat /var/log/celery/worker1.log`
You should see the results of your task.

    [2014-08-30 06:16:40,493: INFO/MainProcess] Received task: myapp.add[1e880570-24b5-4bf8-8fe2-a72387ecb709]
    [2014-08-30 06:16:40,494: INFO/MainProcess] Task myapp.add[1e880570-24b5-4bf8-8fe2-a72387ecb709] succeeded in 0.000346501000422s: 14
    
Now that you know how to run a celery task you can edit myapp.py and add a task of your own.

Have Fun!
