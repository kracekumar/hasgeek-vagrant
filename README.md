Repo contains scripts to make hasgeek development with vagrant, vm easier.

**Please don't clone this directory for set up**

Instructions
-----
1. Install [vagrant](http://downloads.vagrantup.com/tags/v1.2.2) and [virtualbox](https://www.virtualbox.org/wiki/Downloads).
2. `cd ~` # go to home directory
3. `wget https://raw.github.com/kracekumar/hasgeek-vagrant/master/startup.py https://raw.github.com/kracekumar/hasgeek-vagrant/master/startup.sh https://raw.github.com/kracekumar/hasgeek-vagrant/master/Vagrantfile`
4. `vagrant plugin install vagrant-hostsupdater`
5. `vagrant up`
6. `sudo pip install fabric`
7. `fab -f startup.py local clone_hasgeek_dependencies clone_hasgeek_repos`
# Everytime git clones a repo, passaphrase is prompted. It is annoying. Will be fixed in upcoming release
8. `vagrant ssh`
9. `cd /vagrant/hasgeek` is where all hasgeek code base is located.
10. `sudo fab -f startup.py local vagrant install`
11. Create new database user. `sudo -u postgres createuser -D -A -P hasgeek` with password `hasgeek`.
12. `hacknight.local`, `hasgeek.tv.local`, `imgee.local`, `kharcha.local`, `hasjob.local` are added to `/etc/hosts`
