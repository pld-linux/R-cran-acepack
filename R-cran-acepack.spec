%define		fversion	%(echo %{version} |tr r -)
%define		modulename	acepack
Summary:	ace() and avas() for selecting regression transformations
Summary(pl.UTF-8):	ace() i avas() do wyboru przekształceń regresji
Name:		R-cran-%{modulename}
Version:	1.3r3.3
Release:	2
License:	avas is public domain, ace is on Statlib
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	088bedfe9e976ad15205645f499c842e
BuildRequires:	R >= 2.8.1
BuildRequires:	gcc-fortran
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACE and AVAS methods for choosing regression transformations.

%description -l pl.UTF-8
Metody ACE i AVAS do wyboru przekształceń regresji.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION %{modulename}/README* %{modulename}/ace.doc
%{_libdir}/R/library/%{modulename}
