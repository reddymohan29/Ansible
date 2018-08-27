import sys

domain_home='{{domain_home}}'
aia_template='/u01/app/oracle/soa/installation/weblogic12.1.3/soa/common/templates/wls/oracle.soa.fp_template.jar'
readDomain(domain_home)
addTemplate(aia_template)
updateDomain()
closeDomain()
