%define module reactivex

Summary:	A library for composing asynchronous and event-based programs using observable collections and query operator functions in Python
Name:		python-%{module}
Version:	4.0.4
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://reactivex.io/
Source0:	https://files.pythonhosted.org/packages/source/r/reactivex/reactivex-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:  python3dist(poetry)
BuildRequires:	python3dist(wheel)

%description
ReactiveX for Python (RxPY) is a library for composing asynchronous and event-based programs using observable sequences and pipable query operators in Python. 
Using Rx, developers represent asynchronous data streams with Observables, query asynchronous data streams using operators, and parameterize concurrency in data/event streams using Schedulers.

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
