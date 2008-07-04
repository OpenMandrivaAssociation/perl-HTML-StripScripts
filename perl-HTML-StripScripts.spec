%define module   HTML-StripScripts
%define version    1.04
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Strip scripting constructs out of HTML
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.gz
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

