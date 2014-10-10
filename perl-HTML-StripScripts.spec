%define upstream_name    HTML-StripScripts
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Strip scripting constructs out of HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module strips scripting constructs out of HTML, leaving as much
non-scripting markup in place as possible. This allows web applications to
display HTML originating from an untrusted source without introducing XSS
(cross site scripting) vulnerabilities.

You will probably use the HTML::StripScripts::Parser manpage rather than
using this module directly.

The process is based on whitelists of tags, attributes and attribute
values. This approach is the most secure against disguised scripting
constructs hidden in malicious HTML documents.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 654972
- rebuild for updated spec-helper

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 461286
- update to 1.05

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 403260
- rebuild using %%perl_convert_version

* Fri Jul 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.0
+ Revision: 231906
- import perl-HTML-StripScripts


* Fri Jul 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.0
- initial mdv release, generated with cpan2dist
