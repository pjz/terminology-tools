


import os.path


def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)


def icon(filename):
    """
    Given a filename, return the appropriate xdg icon name for it,
    or None if we don't know what's appropriate
    """
    absname = os.path.abspath(filename)
    # ripped (approximately) from tyls source
    fname = os.path.basename(absname)
    if os.path.isdir(absname):
        return icon_for_dir(fname)
    elif is_exe(absname):
        return icon_for_executable(fname)
    else:
        return icon_for_basic(fname)


def icon_for_dir(name):
    if name == 'Desktop' or name.startswith('Desktop-'):
        return 'user-desktop'
    return 'folder'


def icon_for_executable(name):
    if name.lower().endswith('.sh'):
        return 'text-x-script'
    return 'application-x-executable'


# or: run file -i, extract the mime-type, replace the / with a -
BASIC_EXTS = {
    ".mp3": "audio-x-mpeg",
    ".aac": "audio-x-generic",
    ".wav": "audio-x-wav",
    ".m3u": "audio-x-mp3-playlist",
    ".patch": "text-x-generic",
    ".diff": "text-x-generic",
    ".rpm": "package-x-generic",
    ".srpm": "package-x-generic",
    ".deb": "package-x-generic",
    ".pkg.tar.xz": "package-x-generic",
    ".tar": "application-x-tar",
    ".tgz": "application-x-tar",
    ".tbz": "application-x-tar",
    ".zip": "application-x-zip",
    ".rar": "text-x-generic",
    ".cpio": "text-x-generic",
    ".iso": "application-x-cd-image",
    ".img": "text-x-generic",
    ".ttf": "font-x-generic",
    ".bdf": "font-x-generic",
    ".pcf": "font-x-generic",
    "~": "text-x-generic",
    "tamp-h1": "text-x-generic",
    "akefile": "text-x-generic",
    "akefile.in": "text-x-generic",
    ".am": "text-x-generic",
    ".spec": "text-x-generic",
    ".m4": "application-x-m4",
    ".sh": "text-x-generic",
    ".bin": "text-x-generic",
    ".run": "text-x-generic",
    "onfigure": "text-x-generic",
    "onfigure.in": "text-x-generic",
    "onfigure.ac": "text-x-generic",
    ".in": "text-x-generic",
    ".c": "text-x-c",
    ".x": "text-x-c",
    ".h": "text-x-chdr",
    ".edc": "text-x-generic",
    ".edj": "text-x-generic",
    ".cc": "text-x-c++",
    ".hh": "text-x-c++hdr",
    ".php": "application-x-php",
    ".desktop": "application-x-desktop",
    ".directory": "application-x-desktop",
    ".o": "text-x-generic",
    ".lo": "text-x-generic",
    ".la": "text-x-generic",
    ".log": "text-x-generic",
    ".txt": "text-x-generic",
    ".xml": "text-xml",
    "README": "text-x-generic",
    "Readme": "text-x-generic",
    "readme": "text-x-generic",
    "INSTALL": "text-x-generic",
    "COPYING": "text-x-generic",
    "NEWS": "text-x-generic",
    "ChangeLog": "text-x-changelog",
    "AUTHORS": "text-x-generic",
    "TODO": "text-x-generic",
    ".doc": "x-office-document",
    ".docx": "x-office-document",
    ".html": "text-x-html",
    ".htm": "text-x-html",
    ".css": "text-x-css"
}

def icon_for_basic(name):
    fname = name.lower()
    for ext in BASIC_EXTS:
        if fname.endswith(ext):
            return BASIC_EXTS[ext]
    if '.tar.' in fname:
        return "application-x-tar"
    return None
