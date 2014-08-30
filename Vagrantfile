# -*- mode: ruby -*-
# vi: set ft=ruby :

hosts = {
  "host0.celery" => "192.168.33.10",
}

Vagrant.configure("2") do |config|
  hosts.each do |name, ip|
    config.vm.define name do |machine|
      machine.vm.box = "precise32"
      machine.vm.box_url = "http://files.vagrantup.com/precise32.box"
      machine.vm.hostname = name
      machine.vm.network :private_network, ip: ip
      machine.vm.synced_folder "code/", "/data/code"
      machine.vm.provider "virtualbox" do |v|
          v.name = name
          v.customize ["modifyvm", :id, "--memory", 200]
      end
      config.vm.provision "ansible" do |ansible|
          ansible.playbook = "celery.yml"
          ansible.groups = { "celery" => ["host0.celery"] }
      end
    end
  end
end
