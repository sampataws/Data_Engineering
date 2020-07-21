1) sudo wget https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo

2) sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo

3) sudo yum install -y apache-maven

4) mvn --version