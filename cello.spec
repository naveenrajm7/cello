Name:           cello
Version:        1.0.2
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        MIT
URL:            https://github.com/naveenrajm7/%{name}
Source0:        https://github.com/naveenrajm7/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
      

%description
A simple RPM package to print Hello World

%prep
%setup -q 

%build
make %{?_smp_mflags}


%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Wed Mar 25 2020 naveen
- first cello package
