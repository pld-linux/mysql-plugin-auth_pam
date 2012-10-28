Summary:	PAM authentication plugin for MySQL
Name:		mysql-plugin-auth_pam
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/Databases
URL:		http://www.percona.com/
Source0:	http://www.percona.com/downloads/Percona-PAM-plugin/%{version}/source/percona-pam-plugin-%{version}.tar.gz
# Source0-md5:	00b5ee08021435201678d658d36c6d65
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mysql-devel >= 5.5
BuildRequires:	pam-devel
Requires:	mysql >= 5.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Percona PAM plugin enables users to authenticate to the MySQL
server via PAM. This package contains the plugin library, you need to
enable this behaviour in your server by issuing the following command:

INSTALL PLUGIN auth_pam_server SONAME 'auth_pam.so';

%prep
%setup -q -n percona-pam-plugin-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mysql/plugin/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mysql/plugin/test_auth_pam_client.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mysql/plugin/auth_pam.so
