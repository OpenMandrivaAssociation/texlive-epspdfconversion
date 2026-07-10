%global tl_name epspdfconversion
%global tl_revision 18703

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.61
Release:	%{tl_revision}.1
Summary:	On-the-fly conversion of EPS to PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/epspdfconversion
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package calls the epstopdf package to convert EPS graphics to PDF,
on the fly. It servs as a vehicle for passing conversion options (such
as grayscale, prepress or pdfversion) to the epspdf converter.

