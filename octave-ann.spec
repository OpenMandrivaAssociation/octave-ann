%define octpkg ann

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Wraps the ANN library, for Octacew
Name:		octave-%{octpkg}
Version:	1.0.2
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 2.9.12

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Octave-forge ANN package wraps the ANN library, which provides data
structures and functions for computing exact and approximate nearest
neighbors on an arbitrarily high dimensional point set.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

