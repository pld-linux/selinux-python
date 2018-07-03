#
# Conditional build:
%bcond_without	python3	# CPython 3.x modules
#
Summary:	SELinux Python policy utilities
Summary(pl.UTF-8):	Narzędzia do polityk SELinuksa napisane w Pythonie
Name:		selinux-python
Version:	2.7
Release:	3
License:	GPL v2 (sepolgen), GPL v2+ (semodule, sepolicy)
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://raw.githubusercontent.com/wiki/SELinuxProject/selinux/files/releases/20170804/%{name}-%{version}.tar.gz
# Source0-md5:	b118229d34a6aec34471c3c2c9cac172
Patch0:		%{name}-pythondir.patch
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	libsepol-static >= 2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	policycoreutils >= 2.7
Requires:	python-sepolicy = %{version}-%{release}
Obsoletes:	policycoreutils-sepolicy < 2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains Python based SELinux policy utilities.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera narzędzia do polityk SELinuksa napisane w Pythonie.

%package -n bash-completion-%{name}
Summary:	Bash completion for semanage and sepolicy commands
Summary(pl.UTF-8):	Bashowe dopełnianie składni poleceń semanage i sepolicy
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2

%description -n bash-completion-%{name}
Bash completion for semanage and sepolicy commands.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe dopełnianie składni poleceń semanage i sepolicy.

%package -n python-sepolgen
Summary:	sepolgen - Python 2 module for policy generation
Summary(pl.UTF-8):	Moduł Pythona 2 sepolgen do generowania polityki
License:	GPL v2
Group:		Python/Libraries
Requires:	python-selinux >= 2.7
Requires:	python-sepolgen-common = %{version}-%{release}
Suggests:	python-setools
BuildArch:	noarch

%description -n python-sepolgen
sepolgen - Python module for policy generation.

%description -n python-sepolgen -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

%package -n python-sepolgen-common
Summary:	Common files for sepolgen Python modules
Summary(pl.UTF-8):	Pliki wspólne dla modułów Pythona sepolgen
License:	GPL v2
Group:		Development/Languages/Python

%description -n python-sepolgen-common
Common files for sepolgen Python modules.

%description -n python-sepolgen-common -l pl.UTF-8
Pliki wspólne dla modułów Pythona sepolgen.

%package -n python3-sepolgen
Summary:	sepolgen - Python 3 module for policy generation
Summary(pl.UTF-8):	Moduł Pythona 3 sepolgen do generowania polityki
License:	GPL v2
Group:		Python/Libraries
Requires:	python-sepolgen-common = %{version}-%{release}
Requires:	python3-selinux >= 2.7
# TODO: uncomment when setools supports python 3 (3.3.8 doesn't)
#Suggests:	python-setools
BuildArch:	noarch

%description -n python3-sepolgen
sepolgen - Python module for policy generation.

%description -n python3-sepolgen -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

%package -n python-sepolicy
Summary:	Python modules for SELinux policy manipulation
Summary(pl.UTF-8):	Moduły Pythona do operowania na politykach SELinuksa
Group:		Python/Libraries
# seobject and sepolicy use translations from policycoreutils domain
Requires:	policycoreutils >= 2.7
Requires:	python-IPy
Requires:	python-dbus
Requires:	python-semanage >= 2.7
Requires:	python-sepolgen = %{version}-%{release}
Requires:	python-setools
Requires:	python-slip-dbus
# for sepolicy.gui additionally:
Requires:	gtk+3 >= 3
Requires:	python-pygobject3 >= 3
Obsoletes:	python-sepolgen < 2.7
Conflicts:	policycoreutils-sepolicy < 2.7

%description -n python-sepolicy
Python modules for SELinux policy manipulation.

%description -n python-sepolicy -l pl.UTF-8
Moduły Pythona do operowania na politykach SELinuksa.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} \
	CC="%{__cc}" \
	LIBDIR="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHONLIBDIR=%{py_sitescriptdir} \
	LIBSEPOLA=%{_libdir}/libsepol.a

#py_comp $RPM_BUILD_ROOT%{py_sitedir}
#py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%if %{with python3}
%{__make} -C sepolgen/src/sepolgen install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHONLIBDIR=%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audit2allow
%attr(755,root,root) %{_bindir}/audit2why
%attr(755,root,root) %{_bindir}/chcat
%attr(755,root,root) %{_bindir}/sepolgen
%attr(755,root,root) %{_bindir}/sepolgen-ifgen
%attr(755,root,root) %{_bindir}/sepolgen-ifgen-attr-helper
%attr(755,root,root) %{_bindir}/sepolicy
%attr(755,root,root) %{_sbindir}/semanage
%{_mandir}/man1/audit2allow.1*
%{_mandir}/man1/audit2why.1*
%{_mandir}/man8/chcat.8*
%{_mandir}/man8/sepolgen.8*
%{_mandir}/man8/sepolicy*.8*
%{_mandir}/man8/semanage*.8*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/semanage
%{bash_compdir}/sepolicy

%files -n python-sepolgen
%defattr(644,root,root,755)
%{py_sitescriptdir}/sepolgen

%files -n python-sepolgen-common
%defattr(644,root,root,755)
%dir /var/lib/sepolgen
%config(noreplace) %verify(not md5 mtime size) /var/lib/sepolgen/perm_map

%files -n python3-sepolgen
%defattr(644,root,root,755)
%{py3_sitescriptdir}/sepolgen

%files -n python-sepolicy
%defattr(644,root,root,755)
%{py_sitescriptdir}/seobject.py[co]
%dir %{py_sitedir}/sepolicy
%{py_sitedir}/sepolicy/*.py[co]
%{py_sitedir}/sepolicy/sepolicy.glade
%dir %{py_sitedir}/sepolicy/help
%{py_sitedir}/sepolicy/help/__init__.py[co]
%{py_sitedir}/sepolicy/help/*.png
%{py_sitedir}/sepolicy/help/*.txt
%dir %{py_sitedir}/sepolicy/templates
%{py_sitedir}/sepolicy/templates/*.py[co]
%{py_sitedir}/sepolicy-1.1-py*.egg-info
