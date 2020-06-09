Name:           rover
Version:        1.0.1
Release:        1%{?dist}
Summary:        Rover is a file browser for the terminal.

License:        Public Domain
URL:            https://github.com/lecram/%{name}
Source0:        %{URL}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel
BuildRequires:  gcc

%description
Rover has a Terminal User Interface (TUI) designed to fit in a small terminal window. There are ten tabs, but only one is visible at each time, selected by keys 0-9. The number of the current active/visible tab is shown at the top-right corner. The starting path for each tab can be given as command-line arguments; unassigned tabs will start at the current working directory. The current directory of the active tab is shown at the top of the screen.

%prep
%autosetup
sed -i 's/^PREFIX=.*/PREFIX=\%{_prefix}/' Makefile
sed -i 's|^MANPREFIX=.*|MANPREFIX=%{_mandir}|' Makefile

%build
%set_build_flags
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc %{_mandir}/man1/%{name}*
%doc README.md FAQ.md
%_bindir/%name

%changelog
* Tue Jun  9 2020 nasirhm <nasirhm@fedoraproject.org>
- Inital Package
