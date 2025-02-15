# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.6.3] 2023-09-02

### Changed

- bump chromadb to 0.4.8

### Fixed

- fix depenencies for python 3.11
- add explicit dependency on wrapt

## [0.6.2] 2023-09-01

### Added

- `output_parsers.parser_lib.get_rich_md` to sanitize agent output to markdown 
- wip: REPL input modes and auto completion
- wip: Programming assistant agent
- Progress bar for async events on tools
- select and edit source documents used for retrieval Q&A with ctrl+p
- Retrieval Q&A with agents returns source documents
- `ProgressBar` protocol and wrapper to use Textual progress bar in a thread safe way
  and hook into tqdm update events.
- Edit input using an external `$EDITOR` with `ctrl+e`
- Capture and redirect logging/output to NeuronCLI console widget.
- Generate sphinx doc for online and offline reading from within the app. 
- wip: offline doc reader: jump to anchors (https://github.com/Textualize/textual/pull/2941)
- Help screen for common keybindings with `?`
- UI: reusable action bar widget.

#### index management: 

- Embeddings: added bge-base embeddings option
- Scan and load multiple PDFs from a directory under a single collection
- `AutoDirLoader`: scan and load a directory, auto detects file types and assigns 
the appropriate splitter based on the detected content type.
- link (patch) the index console progress bar to `tqdm` updates
- progress bar for loading, splitting and indexing files
- added a local file system path selection UI
- chromadb: save/restore used embedding function. You can have multiple indexes using
  different embedding functions.
- Choose to use local embeddings when creating index.
- TODO: detect local embeddings when loading an index.

### Changed

- Refactored the prompt input and console output for better UX.
- Bumped `textual` to version **v0.34.0** (TextLog -> RichLog)
- Improved key bindings
- Memory mixin to handle retrieval answers with source documents
- Retrieval uses MMR search algorithm by default
- Improved form validation
- Upgraded dependencies
- ChromaDB: no more manual call to `persist`

### Fixed

- index: async delete indexes: ensure deletion happens after index is loaded.
- improved iPython dev console: avoid term repaints until end of session.
- Fast preloading of messages when switching agent tab. 
- Chroma: share a single client for all indexes
- Explicit dependency on `sentence-transofmers` library for local embeddings.
- Many fixes related to dependency updates

## [0.5.0] - 2023-07-18

### Added

- Github action for generating online sphinx documentation 

### Changed

- Bumped `textual` to version **v0.29.0**
