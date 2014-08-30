qwikcelery
==========

Vagrant Ansible VM for developing with celery

# Installing Vagrant

In order to run Vagrant, you need:

- VirtualBox installed
- Ruby installed (should be on your system already)
- Vagrant 1.1+ installed (see
  http://docs.vagrantup.com/v2/installation/index.html).

This should be all it takes to set up Vagrant.

Now bootstrap your virtual machines with the following command. Note that you do not need to download any "box" manually. This project already includes a `Vagrantfile` to get you up and running, and will get one for you if needed.

`vagrant up`

and go grab yourself a coffee (note that if you use vagrant-hostmaster, you'll need 
to type your password since it needs to sudo as root).

If something goes wrong, refer to Vagrant's [Getting Started
Guide](http://docs.vagrantup.com/v2/getting-started/index.html).

# Adding your SSH keys on the virtual machines

To follow this tutorial, you'll need to have your keys in VMs root's `authorized_keys`. 
While this is not absolutely necessary (Ansible can use sudo, password authentication, 
etc...), it will make things way easier.

Ansible is perfect for this and we will use it for the job. From the qwikcelery project directory:

    ansible-playbook -c paramiko -i ips setup.yml --ask-pass --sudo

When asked for password, enter _vagrant_. If you get errors wait a minute and try again...sometimes this takes two tries for me.

Once that command runs successfully you can setup the VM by running:

    ansible-playbook -i hosts celery.yaml
    
When that finishes if there wre no errors you can 

    vagrant up
    
and get to the celery goodness.


Thanks to [Michel Blanc](https://github.com/leucos) and the other [contributors](https://github.com/leucos/ansible-tuto/graphs/contributors) to [ansible-tuto](https://github.com/leucos/ansible-tuto) for the tutorial and free code.
