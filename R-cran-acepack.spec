%define		fversion	%(echo %{version} |tr r -)
%define		modulename	acepack
Summary:	ace() and avas() for selecting regression transformations
Summary(pl):	ace() i avas() do wyboru przekszta³ceñ regresji
Name:		R-cran-%{modulename}
Version:	1.3r2.1
Release:	1
License:	avas is public domain, ace is on Statlib
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	eb75cab587664b58df4a14c65f450b62
BuildRequires:	R-base >= 2.0.0
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACE and AVAS methods for choosing regression transformations.

%description -l pl
Metody ACE i AVAS do wyboru przekszta³ceñ regresji.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION %{modulename}/README* %{modulename}/ace.doc
%{_libdir}/R/library/%{modulename}
