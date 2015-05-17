Project P2: Tournament Results

Description
A Python module that uses PostgreSQL database schema to store tournaments results,
while creating a list to pair off matches using the Swiss Pairing methods of matching
players with similar results.

Prerequisites
- VirtualBox
- Vagrant

Instructions
1. Clone this repo to your project folder
2. Open terminal and navigate to your project directory
	ie: cd full stack/vagrant
3. type:	
	vagrant up
4. After vagrant is running type:
	vagrant ssh
5. Set up PostgreSQL by typing
	cd /vagrant/tournament -> psql
	-> create database tournament;
	-> \c tournament ->\i tournament.sql -> \q
6. Run test by typing:
	python tournament_test.py
7. If program is running properly all 8 tests will pass

If you have any questions please email
toddrushing@toddrushing.com

