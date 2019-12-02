# Scylla

## About
CLI client for scylla.sh written in Python
Written by k0fin

## Requirements & Installation

    $ sudo apt-get -y install git python-pip
    $ sudo git clone https://github.com/k0fin/scylla.git
    $ cd scylla
    $ pip install -r requirements.txt
    $ python setup.py install
    $ scylla --help

## Breach Databases

Scylla can search the following available databases:

    * xhamster
    * aimjunkies
    * xsplit
    * 000webhost
    * edmodo
    * abandonia
    * exploit
    * 7k7k
    * tumblr
    * zoosk
    * myspace
    * dropbox
    * badoo_normalized
    * linkedin
    * lastfm
    * twitter
    * webhostingtalk
    * cdprojektred

## Supported Query Types

The Scylla CLI tool supports the same Lucene syntax supported by the front-end web application:

    * Email
    * UserId
    * User
    * Name
    * IP
    * PassHash
    * Password
    * PassSalt
    * Domain

## Usage

    * Asdf

## Todo

    * Automatic passive hash lookups
