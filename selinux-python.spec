Summary:	SELinux Python policy utilities
Summary(pl.UTF-8):	Narzędzia do polityk SELinuksa napisane w Pythonie
Name:		selinux-python
Version:	2.9
Release:	2
License:	GPL v2 (sepolgen), GPL v2+ (semodule, sepolicy)
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/20190315/%{name}-%{version}.tar.gz
# Source0-md5:	e9dfedd1139dd9998f5a09abfb670454
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	libsepol-static >= 2.7
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	policycoreutils >= 2.7
Requires:	python3-sepolicy = %{version}-%{release}
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

%package -n python3-sepolgen
Summary:	sepolgen - Python 3 module for policy generation
Summary(pl.UTF-8):	Moduł Pythona 3 sepolgen do generowania polityki
License:	GPL v2
Group:		Libraries/Python
Requires:	python3-selinux >= 2.7
Suggests:	python3-setools
Obsoletes:	python-sepolgen-common < 2.9-1
BuildArch:	noarch

%description -n python3-sepolgen
sepolgen - Python module for policy generation.

%description -n python3-sepolgen -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

%package -n python3-sepolicy
Summary:	Python modules for SELinux policy manipulation
Summary(pl.UTF-8):	Moduły Pythona do operowania na politykach SELinuksa
Group:		Libraries/Python
# seobject and sepolicy use translations from policycoreutils domain
Requires:	policycoreutils >= 2.7
Requires:	python3-IPy
Requires:	python3-dbus
Requires:	python3-semanage >= 2.7
Requires:	python3-sepolgen = %{version}-%{release}
Requires:	python3-setools
Requires:	python3-slip-dbus
# for sepolicy.gui additionally:
Requires:	gtk+3 >= 3
Requires:	python3-pygobject3 >= 3
Conflicts:	policycoreutils-sepolicy < 2.7

%description -n python3-sepolicy
Python modules for SELinux policy manipulation.

%description -n python3-sepolicy -l pl.UTF-8
Moduły Pythona do operowania na politykach SELinuksa.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} \
	CC="%{__cc}" \
	LIBDIR="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHONLIBDIR=%{py3_sitescriptdir} \
	LIBSEPOLA=%{_libdir}/libsepol.a

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
%lang(ru) %{_mandir}/ru/man*/*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/semanage
%{bash_compdir}/sepolicy

%files -n python3-sepolgen
%defattr(644,root,root,755)
%{py3_sitescriptdir}/sepolgen
%dir /var/lib/sepolgen
%config(noreplace) %verify(not md5 mtime size) /var/lib/sepolgen/perm_map

%files -n python3-sepolicy
%defattr(644,root,root,755)
%{py3_sitescriptdir}/seobject.py
%dir %{py3_sitedir}/sepolicy
%{py3_sitedir}/sepolicy/__pycache__
%{py3_sitedir}/sepolicy/*.py
%{py3_sitedir}/sepolicy/sepolicy.glade
%dir %{py3_sitedir}/sepolicy/help
%{py3_sitedir}/sepolicy/help/__pycache__
%{py3_sitedir}/sepolicy/help/__init__.py
%{py3_sitedir}/sepolicy/help/*.png
%{py3_sitedir}/sepolicy/help/*.txt
%dir %{py3_sitedir}/sepolicy/templates
%{py3_sitedir}/sepolicy/templates/__pycache__
%{py3_sitedir}/sepolicy/templates/*.py
%{py3_sitedir}/sepolicy-1.1-py*.egg-info
