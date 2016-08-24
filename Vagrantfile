# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set nu :

PROJECT_NAME = "lectureskpd"
LECTURES = ENV["LECTURES"]

Vagrant.configure(2) do |config|
  config.vm.synced_folder ".",
      "/home/vagrant/lectureskpd/"

  # Lectures docs
  config.vm.define 'lectureskpd', primary: true do |lectureskpd|

    lectureskpd.ssh.port = 22
    lectureskpd.ssh.username = 'vagrant'
    lectureskpd.ssh.password = '123'

    lectureskpd.vm.provision :shell, privileged: false,
      :path => "vagrant/docker/lectureskpd/build-docs.sh",
      :env => {LECTURES: LECTURES}

    lectureskpd.vm.provider 'docker' do |docker|
      docker.name = PROJECT_NAME
      docker.build_dir = './vagrant/docker/lectureskpd/'
      docker.build_args = ['--tag=ustu/lectureskpd']
      docker.remains_running = false

      # -t - Allocate a (pseudo) tty
      # -i - Keep stdin open (so we can interact with it)
      docker.create_args = ['-i', '-t']
      docker.has_ssh = true
    end
  end
end
