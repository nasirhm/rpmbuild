%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from
%distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%global srcname mote

Name:           %{srcname}
Version:        0.6.3
Release:        4%{?dist}
Summary:        A MeetBot log wrangler, providing a user-friendly interface for Fedora's logs

License:        GPLv2+
URL:            https://github.com/nasirhm/mote
Source0:        https://github.com/nasirhm/mote/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-mod_wsgi
BuildRequires:  python3-flask
BuildRequires:  python3-fedora
BuildRequires:  python3-fedora-flask
BuildRequires:  python3-openid
BuildRequires:  python3-memcached
BuildRequires:  python3-openid-cla
BuildRequires:  python3-openid-teams
BuildRequires:  python3-requests
BuildRequires:  python3-dateutil
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-six
BuildRequires:  python3-arrow
BuildRequires:  fedmsg

# For rpm macros, so we know where to install the service file.
BuildRequires:  systemd

Requires: python3
Requires: python3-pip
Requires: python3-mod_wsgi
Requires: python3-flask
Requires: python3-openid
Requires: python3-memcached
Requires: python3-fedora
Requires: python3-openid-cla
Requires: python3-openid-teams
Requires: python3-requests
Requires: python3-dateutil
Requires: python3-beautifulsoup4
Requires: python3-fedora-flask
Requires: python3-six
Requires: python3-arrow
Requires: fontawesome-fonts
Requires: fontawesome-fonts-web
Requires: fedmsg

%description
A Meetbot log wrangler, providing a user-friendly interface for
Fedora Project's logs. mote allows contributors to the Fedora Project to
quickly search and find logs beneficial in keeping up to daye with the
project's activities.

%prep
%autosetup -n %{name}-%{version}
rm -rf *.egg*

%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT

# Install apache configuration file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/
install -m 644 files/mote.conf $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/mote.conf

# Install mote configuration file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mote
install -m 644 files/config.py $RPM_BUILD_ROOT/%{_sysconfdir}/mote/config.py

# Install mote wsgi file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mote
install -m 644 files/mote.wsgi $RPM_BUILD_ROOT/%{_datadir}/mote/mote.wsgi

# Remove bundled font files
rm -rf %{buildroot}/%{python_sitelib}/mote/static/fonts

# Symlink font files
#ln -s /usr/share/fonts/fontawesome %{buildroot}%{python_sitelib}/mote/static/fonts

# systemd service file for fedmsg cache updater
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__install} -pm644 files/mote-updater.service \
    %{buildroot}%{_unitdir}/mote-updater.service

%files
%doc README.md
%{!?_licensedir:%global license %doc}
%license LICENSE
%dir %{_sysconfdir}/mote/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mote.conf
%config(noreplace) %{_sysconfdir}/mote/config.py
%config(noreplace) %{_sysconfdir}/mote/config.pyc
%config(noreplace) %{_sysconfdir}/mote/config.pyo
%{_datadir}/mote
%{_datadir}/mote-updater.service
%{python_sitelib}/mote/
%{python_sitelib}/mote*.egg-info
%{_bindir}/mote-updater

%changelog
* Mon Dec  7 2020 nasirhm <nasirhussainm14@gmail.com>
- Initialized
