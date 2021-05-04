# Security Policy

## Overview
Web application vulnerabilities account for the largest portion of attack vectors outside of malware.
It is crucial that any web application be assessed for vulnerabilities and any vulnerabilities be remediated
prior to production deployment. The purpose of this policy is to define web application security assessments
within Foodle application during and after development.

## Scope
All web application security activities will be performed solely on the scope of the Foodle project assets by
delegated quality assurance personnel actively participating on Foodle project development. All findings are
considered confidential and are to be distributed to persons on a “need to know” basis. Distribution of any
findings outside of Foodle project is strictly prohibited unless approved by the project lead.

All security issues that are discovered during testing must be mitigated based upon the following risk levels.
The Risk Levels are based on the OWASP Risk Rating Methodology. Remediation validation testing will be required
to validate fix and/or mitigation strategies for any discovered issues of Medium risk level or greater.

## Security Assesments
Foodle project security assessments are based on the following criteria:
- **Vulnerability Management:**
  - Risk Rankings - All the vulnerabilities would be assigned a risk ranking such as High, Medium and Low based
  on industry best practices such as CVSS base score:
    - High - Any high risk issue must be fixed immediately or other mitigation strategies must be put in place to
    limit exposure before deployment. Applications with high risk issues are subject to being taken off-line or
    denied release into the live environment.
    - Medium - Medium risk issues should be reviewed to determine what is required to mitigate and scheduled accordingly.
    Applications with medium risk issues may be taken off-line or denied release into the live environment based on the
    number of issues and if multiple issues increase the risk to an unacceptable level. Issues should be fixed in a
    patch/point release unless other mitigation strategies will limit exposure.
    - Low - Issue should be reviewed to determine what is required to correct the issue and scheduled accordingly.
  - Vulnerability Scanning - Following the recommendations in OWASP Top 10 standard awareness document, the Foodle
  team will run internal vulnerability scan and web application penetration test, once the project reaches MVP
  functionality levels. The scan process has to include that re-scans will be done until passing results are obtained.
  
- **Secure SDLC:**
  Secure Application Development policy is a plan of action to guide developers’ decisions and actions during the
  software development lifecycle (SDLC) to ensure software security.
  - Secure Coding:
    - Development - Development of code shall be peer reviewed and validated using the the most current version of the
    [Coding Standards for Secure Application Development](https://security.berkeley.edu/secure-coding-practice-guidelines).
    All application developers shall verify that their code is in compliance with the most recent and approved coding
    standards and guidelines.
    - Code Review - Only code validated by the Foodle project team members responsible for quality assurance shall be
    implemented into the production environment - main branch of the GitHub and Heroku code repositories.
  - Application Testing:
    - Methodology - Tests must be conducted at application level and must ensure that at least the
    [OWASP Top Ten vulnerabilities](https://owasp.org/www-project-top-ten/) are addressed.
    - Documentation - All findings or vulnerabilities identified during the tests carried out will be documented with
    sufficient evidence as Issues in the projects GitHub repository. Project maintainer with admin rights is responsible\
    for [creating a security advisory](https://docs.github.com/en/code-security/security-advisories/creating-a-security-advisory)
  - Change Management:
    - Version Control - Any application change and/or update shall be controlled with the GitHub version control and source code
    management system.
    - Audit - All change requests shall be logged whether approved or rejected in GitHub. No single person should be able to
    implement changes to the production version (main branch) of the application without the approval of QA personnel.
    - Testing - Changes shall be tested in an isolated, controlled, and representative environment prior to implementation to
    minimize the effect on the production version of the application, to assess its impact on functionality and security and to
    verify that only intended and approved changes were made.
    - Process - Implementation will only be undertaken after appropriate testing. All major changes shall be treated as new
    functionality implementation and shall be established as a separate coding branch.
  - Awareness:
    - Acknowledgement - This security policy document is distributed to all project developers to read. It is required that all
    developers confirm that they understand the content of this security policy document.
    
## Security Assessments Levels
- Full - A full assessment is comprised of tests for all known web application vulnerabilities using both automated and manual
tools based on the [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/). A full assessment will use
manual penetration testing techniques to validate discovered vulnerabilities to determine the overall risk of any and all discovered.
- Quick - A quick assessment will consist of a automated scan of an application for the OWASP Top Ten web application security risks
at a minimum.
- Targeted - A targeted assessment is performed to verify vulnerability remediation changes or new application functionality.

## Security Assesment Tools
- [Kali Linux](https://www.kali.org/) - Debian-based Linux distribution aimed at advanced Penetration Testing and Security Auditing.
Kali contains several hundred tools which are geared towards various information security tasks, such as Penetration Testing, Security
research, Computer Forensics and Reverse Engineering.
- [OWASP ZAP](https://www.zaproxy.org/) - open source web application security scanner. When used as a proxy server it allows the user
to manipulate all of the traffic that passes through it, including traffic using https. It can also run in a ‘daemon’ mode which is then
controlled via a REST Application programming interface.
- [OWASP Juice Shop](https://juice-shop.herokuapp.com/#/) - Juice Shop is a deliberately insecure web application maintained by OWASP
designed to teach or practice web application security lessons.Foodle project developers can use it to learn hands-on practicing of
vulnerabilities exploitation such as Cross-site scripting, SQL Injections, Buffer Overflow, CSRF, Access Control etc.

Other tools and/or techniques may be used depending upon what is found in the default assessment and the need to determine validity and
risk are subject to the discretion of the Quality assurance team.

## Supported Versions

Following Foodle versions are currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| > 1.0   | :white_check_mark: |
| < 1.0   | :x:                |


## Reporting a Vulnerability (WIP)

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.
