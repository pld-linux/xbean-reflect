#TODO
# - %description/Summary (I need this jar as it is dependency for nexus, but I
# really do not know what it is).
# - Try to recompile it (?)
#
Summary:	XBean reflection
Name:		xbean-reflect
Version:	3.4.3
Release:	0.1
License:	Apache 2.0
Group:		Development/Languages/Java
Source0: http://people.apache.org/repo/m2-ibiblio-rsync-repository/org/apache/xbean/xbean-reflect/3.4.3/xbean-reflect-3.4.3.jar
# Source0-md5:	a52d4ab4c8091cbb3c44efeb65ac3b78
Source1: http://people.apache.org/repo/m2-ibiblio-rsync-repository/org/apache/xbean/xbean-reflect/3.4.3/xbean-reflect-3.4.3-javadoc.jar
# Source1-md5:	3b5b1b4e1eccd855e1bdfb1f9cde9b99
URL:		http://geronimo.apache.org/xbean/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XBean reflection

%package javadoc
Summary:        Online manual for xbean-reflection
Summary(pl.UTF-8):      Dokumentacja online dla xbean-reflection
Group:          Documentation
Requires:       jpackage-utils

%description javadoc
Documentation for xbean-reflection.

%description javadoc -l pl.UTF-8
Dokumentacja dla xbean-reflection.

%prep
%setup -T -c -a 1
rm -rf META-INF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %SOURCE0 $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
