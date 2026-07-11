%global tl_name makecell
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1e
Release:	%{tl_revision}.1
Summary:	Tabular column heads and multilined cells
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makecell
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecell.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecell.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package supports common layouts for tabular column heads in whole
documents, based on one-column tabular environment. In addition, it can
create multi-lined tabular cells. The Package also offers: a macro which
changes the vertical space around all the cells in a tabular environment
(similar to the function of the tabls package, but using the facilities
of the array) macros for multirow cells, which use the facilities of the
multirow package; macros to number rows in tables, or to skip cells;
diagonally divided cells; horizontal lines in tabular environments with
defined thickness.

