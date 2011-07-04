%define		svnrev	108
%define		rel		0.1
Summary:	End-to-end real-world web page instrumentation and measurement suite
Name:		jiffy-web
Version:	0.1
Release:	%{svnrev}.%{rel}
License:	Apache v2.0
Group:		Applications/WWW
# revno=108
# svn co http://jiffy-web.googlecode.com/svn/trunk${revno:+@$revno} jiffy-web
# tar -cjf jiffy-web-$(svnversion jiffy-web).tar.bz2 --exclude-vcs jiffy-web
# ../dropin jiffy-web-$(svnversion jiffy-web).tar.bz2 &
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	b28a09f2daa00de13889d35d2c6464b8
URL:		http://code.google.com/p/jiffy-web/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Jiffy allows developers to:
- measure individual pieces of page rendering (script load, AJAX
  execution, page load, etc.) on every client
- report those measurements and other metadata to a web server
- aggregate web server logs into a database
- generate reports

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a database ingestor javascript reporting $RPM_BUILD_ROOT%{_appdir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.txt
%defattr(-,root,root,-)
%{_appdir}
%{_examplesdir}/%{name}-%{version}
