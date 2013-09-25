%global packname  logspline
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.1.5
Release:          1
Summary:          Logspline density estimation routines
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/logspline_2.1.5.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Routines for the logspline density estimation. oldlogspline uses the same
algorithm as the logspline 1.0.x package - the Kooperberg and Stone (1992)
algorithm (with an improved interface). The recomended routine logspline
uses an algorithm from Stone et al (1997).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
