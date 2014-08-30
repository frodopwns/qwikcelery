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


[Get Started Using Celery](https://github.com/frodopwns/qwikcelery/tree/master/code)


Thanks to [Michel Blanc](https://github.com/leucos) and the other [contributors](https://github.com/leucos/ansible-tuto/graphs/contributors) to [ansible-tuto](https://github.com/leucos/ansible-tuto) for the tutorial and free code.
