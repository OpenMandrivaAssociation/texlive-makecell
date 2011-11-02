Name:		texlive-makecell
Version:	0.1e
Release:	1
Summary:	Tabular column heads and multilined cells
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makecell
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecell.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecell.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package supports common layouts for tabular column heads
in whole documents, based on one-column tabular environment. In
addition, it can create multi-lined tabular cells. The Package
also offers: -- a macro which changes the vertical space around
all the cells in a tabular environment (similar to the function
of the tabls package, but using the facilities of the array); -
- macros for multirow cells, which use the facilities of the
multirow package; -- macros to number rows in tables, or to
skip cells; -- diagonally divided cells; and -- horizontal
lines in tabular environments with defined thickness.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makecell/makecell.sty
%doc %{_texmfdistdir}/doc/latex/makecell/README
%doc %{_texmfdistdir}/doc/latex/makecell/makecell-rus.pdf
%doc %{_texmfdistdir}/doc/latex/makecell/makecell-rus.tex
%doc %{_texmfdistdir}/doc/latex/makecell/makecell.pdf
#- source
%doc %{_texmfdistdir}/source/latex/makecell/makecell.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}