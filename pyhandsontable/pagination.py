from IPython.display import display
import math

from .core import view_table


class PagedViewer:
    chunk_size = 10
    i = 0

    def __init__(self,
                 records,
                 chunk_size=10,
                 **kwargs):
        self.records = list(records)
        self.chunk_size = chunk_size
        self.viewer_kwargs = kwargs
        self.viewer_kwargs.setdefault('config', dict()).setdefault('rowHeaders', False)

    @property
    def num_pages(self):
        return math.ceil(len(self.records) / self.chunk_size)

    @property
    def num_records(self):
        return len(self.records)

    def __len__(self):
        return self.num_records

    def _repr_html_(self):
        display(self.view())
        return ''

    def view(self, page_number = None, start = None):
        """Choose a page number to view

        Keyword Arguments:
            page_number {int >= -1} -- Page number to view (default: {self.i})
            start {int} -- Sequence of the record to start viewing (default: {None})

        Returns:
            Viewer function object
        """

        if page_number is None:
            page_number = self.i
        elif page_number == -1:
            page_number = self.num_pages -1

        self.i = page_number

        if start is None:
            start = page_number * self.chunk_size

        return view_table(self.records[start: start + self.chunk_size], **self.viewer_kwargs)

    def next(self):
        """Shows the next page

        Returns:
            Viewer function object
        """

        if len(self.records) < (self.i + 1) * self.chunk_size:
            self.i = 0
        else:
            self.i += 1

        return self.view()

    def previous(self):
        """Show the previous page

        Returns:
            Viewer function object
        """

        self.i -= 1
        if self.i < 0:
            self.i = self.num_pages - 1

        return self.view()

    def first(self):
        """Shows the first page

        Returns:
            Viewer function object
        """

        return self.view(0)

    def last(self):
        """Shows the last page

        Returns:
            Viewer function object
        """

        return self.view(-1)
