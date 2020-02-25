FROM jenkins/jenkins:lts

ENV CASC_JENKINS_CONFIG="/var/jenkins_home/jenkins.yaml"

COPY ./master/plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY ./master/jenkins.yaml ${CASC_JENKINS_CONFIG}
COPY ./master/executors.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY ./master/default-user.groovy /usr/share/jenkins/ref/init.groovy.d/

USER jenkins

# Installing the plugins we need using the in-built install-plugins.sh script
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Setting up environment variables for Jenkins admin user
ENV JENKINS_USER admin
ENV JENKINS_PASS admin

# Skip initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

VOLUME /var/jenkins_home
