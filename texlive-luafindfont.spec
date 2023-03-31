Name:		texlive-luafindfont
Version:	64936
Release:	2
Summary:	Search fonts in the LuaTeX font database
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luafindfont
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luafindfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luafindfont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This Lua script searches for fonts in the font database.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/luafindfont
%doc %{_texmfdistdir}/texmf-dist/doc/support/luafindfont
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/luafindfont.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/luafindfont.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
