### RPM external libungif 4.1.4

Source: http://switch.dl.sourceforge.net/sourceforge/giflib/%{n}-%{realversion}.tar.gz

%prep
%setup -n %n-%{realversion}

%build
./configure --prefix=%{i} --disable-static
make %makeprocesses

%install
make install
# Strip libraries, we are not going to debug them.
%define strip_files %i/lib
# Drop all the perl scripts. They are not needed and force the installation of
# more packages on Ubuntu.
%define drop_files %i/bin
